"""
https://sites.google.com/chromium.org/driver/downloads

"""




url = "https://www.weebookinn.com/requests"


from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_value(value)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
driver.get("http://www.google.com")
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
element = driver.find_element_by_css_selector("input#passwd-id")
element.send_keys("some text")

elements = {
    'firstname': '<input class="field-element field-control" name="fname" x-autocompletetype="given-name" type="text" spellcheck="false" maxlength="30" data-title="First" aria-required="true">',
    'lastname': '<input class="field-element field-control" name="lname" x-autocompletetype="surname" type="text" spellcheck="false" maxlength="30" data-title="Last" aria-required="true">',
    'email': '<input class="field-element" id="email-yui_3_17_2_1_1434575698341_290495-field" name="email" type="email" autocomplete="email" spellcheck="false" aria-required="true">',
    'phone_areacode': '<input class="field-element" x-autocompletetype="phone-area-code" type="text" maxlength="3" data-title="Areacode" aria-required="true">',
    'phone_prefix': '<input class="field-element" x-autocompletetype="phone-local-prefix" type="text" maxlength="3" data-title="Prefix" aria-required="true">',
    'phone_suffix': '<input class="field-element" x-autocompletetype="phone-local-suffix" type="text" maxlength="4" data-title="Line" aria-required="true">',
    'location': """
        <select id="select-yui_3_17_2_1_1434575698341_304999-field" name="select-yui_3_17_2_1_1434575698341_304999-field" aria-required="true">                  
            <option value="Whyte Avenue">Whyte Avenue</option>  
            <option value="Jasper Avenue">Jasper Avenue</option>
            <option value="Mail Order via Canada Post">Mail Order via Canada Post</option>
          <optgroup label=""></optgroup>
        </select>""",
    'booktitle': '<input class="field-element text" type="text" id="text-yui_3_17_2_1_1434575698341_302759-field" aria-required="true">',
    'author_firstname': '<input class="field-element field-control" name="fname" x-autocompletetype="given-name" type="text" spellcheck="false" maxlength="30" data-title="First">',
    'author_lastname': '<input class="field-element field-control" name="lname" x-autocompletetype="surname" type="text" spellcheck="false" maxlength="30" data-title="Last">',
    'select_pocketbook': '<input type="checkbox" name="checkbox-yui_3_17_2_1_1434575698341_304313-field" value="Pocketbook (small format paperback; approx. 4.25” x 6.87”)">'
    'select_softcover': '<input type="checkbox" name="checkbox-yui_3_17_2_1_1434575698341_304313-field" value="Softcover (large format paperback; approx. 6” x 9”)">',
    'select_hardcover': '<input type="checkbox" name="checkbox-yui_3_17_2_1_1434575698341_304313-field" value="Hardcover">',
    'submit_button': '<input class="button sqs-system-button sqs-editable-button sqs-button-element--primary" type="submit" value="Submit">'
}











