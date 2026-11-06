package com.fashionlooks.aemcloudstarter.core.models;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import io.wcm.testing.mock.aem.junit5.AemContext;
import io.wcm.testing.mock.aem.junit5.AemContextExtension;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

@ExtendWith(AemContextExtension.class)
class PromoModelTest {

    private final AemContext context = new AemContext();

    @BeforeEach
    void setUp() {
        context.addModelsForClasses(PromoModel.class);
    }

    @Test
    void ctaIsValidWhenLabelAndUrlArePresent() {
        context.create().resource("/content/promo",
            "title", "Summer collection",
            "ctaLabel", "Explore",
            "ctaUrl", "/content/site/en/summer.html");

        PromoModel model = context.resourceResolver()
            .getResource("/content/promo")
            .adaptTo(PromoModel.class);

        assertTrue(model.isValidCta());
    }

    @Test
    void ctaIsInvalidWhenUrlIsMissing() {
        context.create().resource("/content/promo",
            "title", "Summer collection",
            "ctaLabel", "Explore");

        PromoModel model = context.resourceResolver()
            .getResource("/content/promo")
            .adaptTo(PromoModel.class);

        assertFalse(model.isValidCta());
    }
}
