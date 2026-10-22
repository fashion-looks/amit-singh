import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template_string

load_dotenv()
app = Flask(__name__)
NASA_API_URL = "https://api.nasa.gov/planetary/apod"
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

HTML = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mind-to-Starlight | Galaxy Controller</title>
<style>
:root{color-scheme:dark;--bg:#030712;--line:#315078;--cyan:#7be7ff;--muted:#a7bad4}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 50% 0,#172b52,#050916 58%,#02040a);color:#edf6ff;font:16px system-ui,sans-serif;min-height:100vh}
#stars{position:fixed;inset:0;width:100%;height:100%;z-index:-1;pointer-events:none}.wrap{max-width:1120px;margin:auto;padding:22px 14px 40px}
header{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:18px}.title{font-size:clamp(1.35rem,4vw,2.1rem);font-weight:800;letter-spacing:.04em}.sub{color:var(--muted);font-size:.9rem;line-height:1.55}
.pill{border:1px solid var(--line);border-radius:99px;padding:7px 11px;color:var(--cyan);font-size:.78rem}
.panel{border:1px solid #5daeff45;background:#091326e8;border-radius:18px;overflow:hidden;box-shadow:0 12px 40px #0005;margin-bottom:15px}.panelhead{padding:14px 16px;border-bottom:1px solid #ffffff14;font-weight:750;letter-spacing:.06em}
.flow{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:9px;padding:16px}.node{min-width:0;border:1px solid var(--line);background:#0a1930;border-radius:13px;padding:13px 8px;text-align:center}.node .ico{font-size:2rem;color:var(--cyan)}.node strong{display:block;font-size:.88rem;margin:7px 0 3px}.node small{color:var(--muted);font-size:.75rem}
.layout{display:grid;grid-template-columns:1fr 1fr;gap:15px}.body{padding:16px}button{background:#0d2543;border:1px solid #7be7ff80;color:#f2f8ff;border-radius:11px;padding:10px 14px;font:inherit;cursor:pointer;transition:.15s}button:hover{background:#16395f;box-shadow:0 0 16px #7be7ff20}button:active{transform:scale(.97)}button.primary{background:linear-gradient(120deg,#075985,#4338a8)}button:disabled{opacity:.5;cursor:wait}
label{display:block;margin:10px 0 7px;color:#d7e7ff;font-size:.9rem}input[type=range]{width:100%;accent-color:var(--cyan)}.meter{height:8px;background:#1b2940;border-radius:9px;overflow:hidden;margin-top:9px}.meter div{height:100%;width:50%;background:linear-gradient(90deg,#8b5cf6,#5be7ff);transition:width .2s}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:14px}.stat{background:#071020;border:1px solid #ffffff13;border-radius:10px;padding:10px}.stat small{color:var(--muted);display:block}.stat strong{display:block;color:var(--cyan);margin-top:5px}
#galaxyCanvas{display:block;width:100%;height:360px;background:radial-gradient(ellipse at center,#0c1c3b,#030712 70%);border-radius:14px}
#apodImage{width:100%;max-height:300px;object-fit:cover;border-radius:12px;display:none;margin-top:12px}#apodTitle{font-size:1.05rem;margin:8px 0}#apodExplanation{color:#c1d0e6;line-height:1.55;font-size:.88rem}
.log{padding:10px;background:#050b16;border-radius:10px;color:#bcd5f4;font:.8rem ui-monospace,monospace;min-height:44px;white-space:pre-wrap}.note{border-left:3px solid #e8c46c;padding:10px 12px;color:#e8dfca;background:#2b251b55;border-radius:0 10px 10px 0;font-size:.82rem;line-height:1.5}
@media(max-width:720px){.flow{grid-template-columns:1fr;gap:8px}.node{display:grid;grid-template-columns:45px 1fr;text-align:left;align-items:center;column-gap:10px}.node .ico{grid-row:span 2}.node strong{margin:0}.node small{font-size:.8rem}.layout{grid-template-columns:1fr}#galaxyCanvas{height:300px}}
</style></head><body><canvas id="stars"></canvas><main class="wrap">
<header><div><div class="title">✦ MIND ↔ STARLIGHT</div><div class="sub">EEG-ready interface • Simulation input available • Public astronomy data</div></div><span class="pill" id="connection">● SIMULATION MODE</span></header>
<section class="panel"><div class="panelhead">AUTOMATIC CONNECTION FLOW</div><div class="flow">
<div class="node"><div class="ico">🧠</div><strong>Brainwaves</strong><small>Future device adapter; no headset connected</small></div>
<div class="node"><div class="ico">〈/〉</div><strong>Python Script</strong><small>App logic and control mapping</small></div>
<div class="node"><div class="ico">☁</div><strong>Internet API</strong><small>Optional public space information</small></div>
<div class="node"><div class="ico">🌌</div><strong>Space Data</strong><small>NASA Astronomy Picture of the Day</small></div>
<div class="node"><div class="ico">▣</div><strong>Visualization</strong><small>Interactive simulated galaxy</small></div>
</div></section>
<section class="panel"><div class="panelhead">GALAXY VISUALIZER</div><div class="body"><canvas id="galaxyCanvas" aria-label="Animated simulated galaxy"></canvas><div class="sub" style="margin-top:8px">The galaxy's glow and rotation respond to the simulated focus control below.</div></div></section>
<div class="layout"><section class="panel"><div class="panelhead">GALAXY CONTROL — SIMULATED INPUT</div><div class="body">
<label for="focus">Focus control: <b id="focusValue">50%</b></label><input id="focus" type="range" min="0" max="100" value="50"><div class="meter"><div id="meter"></div></div>
<div class="row" style="display:flex;gap:8px;margin-top:12px"><button class="primary" id="reset">↻ Reset</button><button id="toggleMotion">Ⅱ Pause motion</button></div>
<div class="stats"><div class="stat"><small>Input source</small><strong>Manual</strong></div><div class="stat"><small>Focus</small><strong id="focusStat">50%</strong></div><div class="stat"><small>EEG status</small><strong>Not connected</strong></div></div>
<p class="sub">This slider is only a simulated input, not a brainwave measurement. A real EEG adapter needs a chosen headset and its supported SDK or stream protocol.</p>
</div></section><section class="panel"><div class="panelhead">NASA SPACE DATA</div><div class="body"><button class="primary" id="loadApod">Load NASA astronomy image</button><p class="sub">Uses the public APOD API; first request may take a moment.</p><div id="apodTitle"></div><div id="apodExplanation"></div><img id="apodImage" alt="NASA astronomy picture of the day"><div class="log" id="status" aria-live="polite">Ready. No API request made yet.</div></div></section></div>
<section class="panel"><div class="panelhead">REAL-WORLD LIMITS</div><div class="body"><div class="note">This application genuinely animates a local galaxy simulation and can fetch NASA APOD data. Because no EEG headset is attached, it does not currently read brain signals. It cannot control physical stars, Earth, or the universe.</div></div></section></main>
<script>
const focus=document.getElementById('focus'),focusValue=document.getElementById('focusValue'),focusStat=document.getElementById('focusStat'),meter=document.getElementById('meter');
let focusLevel=50,paused=false;
focus.addEventListener('input',()=>{focusLevel=Number(focus.value);focusValue.textContent=focusLevel+'%';focusStat.textContent=focusLevel+'%';meter.style.width=focusLevel+'%'});
document.getElementById('reset').addEventListener('click',()=>{focus.value=50;focus.dispatchEvent(new Event('input'));paused=false;document.getElementById('toggleMotion').textContent='Ⅱ Pause motion'});
document.getElementById('toggleMotion').addEventListener('click',()=>{paused=!paused;document.getElementById('toggleMotion').textContent=paused?'▶ Resume motion':'Ⅱ Pause motion'});
document.getElementById('loadApod').addEventListener('click',async()=>{const status=document.getElementById('status'),btn=document.getElementById('loadApod');btn.disabled=true;status.textContent='Requesting NASA APOD data…';try{const r=await fetch('/api/apod');const data=await r.json();if(!r.ok)throw new Error(data.error||'API request failed');document.getElementById('apodTitle').textContent=data.title||'Astronomy Picture of the Day';document.getElementById('apodExplanation').textContent=data.explanation||'';const img=document.getElementById('apodImage');if(data.media_type==='image'&&data.url){img.src=data.url;img.style.display='block'}else{img.style.display='none'}status.textContent='Loaded successfully • '+(data.date||'date unavailable')}catch(e){status.textContent='Could not load data: '+e.message+' — check internet/API limits.'}finally{btn.disabled=false}});
const starCanvas=document.getElementById('stars'),starCtx=starCanvas.getContext('2d');let bgStars=[];
function fitBg(){let d=Math.min(devicePixelRatio||1,2);starCanvas.width=innerWidth*d;starCanvas.height=innerHeight*d;starCanvas.style.width=innerWidth+'px';starCanvas.style.height=innerHeight+'px';starCtx.setTransform(d,0,0,d,0,0);bgStars=Array.from({length:150},()=>({x:Math.random()*innerWidth,y:Math.random()*innerHeight,r:Math.random()*1.4+.2,a:Math.random()*.7+.1,p:Math.random()*7}))}
let bt=0;function drawBg(){starCtx.clearRect(0,0,innerWidth,innerHeight);bgStars.forEach(s=>{starCtx.globalAlpha=s.a*(.65+.35*Math.sin(bt*.01+s.p));starCtx.fillStyle='#d5ecff';starCtx.beginPath();starCtx.arc(s.x,s.y,s.r,0,Math.PI*2);starCtx.fill()});starCtx.globalAlpha=1;bt++;requestAnimationFrame(drawBg)}addEventListener('resize',fitBg);fitBg();drawBg();
const gc=document.getElementById('galaxyCanvas'),gctx=gc.getContext('2d');let points=[],gt=0;
function fitGalaxy(){const d=Math.min(devicePixelRatio||1,2);const r=gc.getBoundingClientRect();gc.width=Math.max(1,r.width*d);gc.height=Math.max(1,r.height*d);gctx.setTransform(d,0,0,d,0,0);points=Array.from({length:950},()=>({a:Math.random()*Math.PI*2,r:Math.pow(Math.random(),.65),arm:Math.floor(Math.random()*4),size:Math.random()*1.5+.3,tw:Math.random()*6.28}))}
function drawGalaxy(){const w=gc.clientWidth,h=gc.clientHeight,cx=w/2,cy=h/2;gctx.clearRect(0,0,w,h);const max=Math.min(w,h)*(.42+focusLevel*.0008),turn=paused?gt:gt*(.002+focusLevel*.000045);const glow=gctx.createRadialGradient(cx,cy,0,cx,cy,max);glow.addColorStop(0,'rgba(255,222,166,.8)');glow.addColorStop(.12,'rgba(101,153,255,.25)');glow.addColorStop(1,'rgba(3,7,18,0)');gctx.fillStyle=glow;gctx.fillRect(0,0,w,h);
points.forEach((p,i)=>{const rr=p.r*max,angle=p.a+p.arm*Math.PI/2+rr*.018+turn,x=cx+Math.cos(angle)*rr,y=cy+Math.sin(angle)*rr*.52;gctx.globalAlpha=.3+.7*(.5+.5*Math.sin(gt*.025+p.tw));gctx.fillStyle=i%7===0?'#fff0bb':(i%3===0?'#a9a1ff':'#7be7ff');gctx.beginPath();gctx.arc(x,y,p.size*(.7+focusLevel/180),0,Math.PI*2);gctx.fill()});gctx.globalAlpha=1;gctx.fillStyle='#fff3d4';gctx.beginPath();gctx.arc(cx,cy,3+focusLevel*.035,0,Math.PI*2);gctx.fill();gt++;requestAnimationFrame(drawGalaxy)}
addEventListener('resize',fitGalaxy);fitGalaxy();drawGalaxy();
</script></body></html>
"""

@app.get("/")
def index():
    return render_template_string(HTML)


@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok", "service": "mind-starlight"}), 200

@app.get("/api/apod")
def apod():
    try:
        response = requests.get(NASA_API_URL, params={"api_key": NASA_API_KEY}, timeout=12)
        response.raise_for_status()
        data = response.json()
        return jsonify({
            "title": data.get("title"), "date": data.get("date"),
            "explanation": data.get("explanation"), "media_type": data.get("media_type"),
            "url": data.get("url"),
        })
    except requests.RequestException:
        app.logger.exception("NASA APOD request failed")
        return jsonify({"error": "NASA API request failed. Check internet access, API key, or rate limit."}), 502
    except ValueError:
        return jsonify({"error": "NASA returned an unexpected response."}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
