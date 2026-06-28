

def test_search_iphone(page):
    page.goto("https://www.noon.com/uae-en/")
    page.fill("#search-input", "iphone")
    page.locator('button').filter(has_text='iphone').first.wait_for()
    page.locator('button').filter(has_text='iphone').nth(2).click()

    try:
        page.locator('button:has-text("ACCEPT ALL")').click(timeout=3000)
    except:
        pass

    first_product = page.locator('[data-qa="plp-product-box-name"]').first
    first_product.wait_for()
    assert first_product.is_visible()
    first_product.click()
    product_title = page.locator('span.ProductTitle-module-scss-module__EXiEUa__title')
    product_title.wait_for()
    assert product_title.is_visible()

    price = page.locator('[data-qa="div-price-now"]')
    assert price.is_visible()

    print("noon iphone test PASSED")



