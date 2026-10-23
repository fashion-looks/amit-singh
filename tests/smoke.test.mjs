import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const html = await readFile(new URL('../index.html', import.meta.url), 'utf8');

test('dashboard has mobile viewport and task form', () => {
  assert.match(html, /name="viewport"/);
  assert.match(html, /id="taskForm"/);
  assert.match(html, /aria-label="Task title"/);
});

test('dashboard includes persistence and CSV export', () => {
  assert.match(html, /localStorage\.setItem/);
  assert.match(html, /Export CSV/);
  assert.match(html, /textContent = task\.text/);
});

test('dashboard has no external script dependencies', () => {
  assert.doesNotMatch(html, /<script[^>]+src=/i);
});
