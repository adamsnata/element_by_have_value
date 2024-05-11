from selene import browser, have, command
from pathlib import Path


def test_register_student():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Aleksei')
    browser.element('#lastName').type('Torsukov')

    browser.element('#userEmail').type('torsukov@gmail.com')

    #      should be #genderWrapper?
    browser.element('#genterWrapper').all('label[for^=gender-radio]').element_by(
        have.text('Male')
    ).click()

    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()

    browser.element('[class$=datepicker]').element('[class$=year-select]').all(
        'option'
    ).element_by(have.value('1911')).click()
    #              OR .text('2000')).click()

    browser.element('[class$=datepicker]').element('[class$=month-select]').all(
        'option'
    ).element_by(have.text('October')).click()

    browser.element('[class$=datepicker]').element('[class$=_month]').all(
        '[role=option][class*=day]'
    ).element_by(have.text('19')).click()

    '''
    OR:
    browser.element('#dateOfBirthInput').type(
        command.Keys.COMMAND + 'a' + command.Keys.NULL + '13 Oct 2000').press_enter()
    '''

    browser.element('#subjectsContainer').click()
    browser.element('#subjectsContainer').element('input').type('Engli').press_tab()

    browser.element('#subjectsContainer').click()
    browser.element('#subjectsContainer').element('input').type(
        'Computer Sci'
    ).press_tab()

    '''
    OR:
    browser.element('#subjectsContainer').click()
    browser.element('#subjectsContainer').element('input').type('Eng')
    browser.element('[class*=subjects][class*=menu-list]').all(
        '[class*=option]'
    ).element_by(have.text('English')).click()
    '''

    browser.element('#hobbiesWrapper').all('[class*=checkbox]').element_by(
        have.text('Sports')
    ).click()

    browser.element('#uploadPicture').type(
        str(Path(__file__).parent.parent.joinpath(f'resources/pic.jpg'))
    )

    browser.element('#currentAddress').type(
        'Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678'
    )

    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#state').element('[class$=menu]').all(
        '[class$=option]'
    ).element_by(have.text('NCR')).click()

    browser.element('#city').click()
    browser.element('#city').element('[class$=menu]').all('[class$=option]').element_by(
        have.text('Delhi')
    ).click()

    browser.element('#submit').click()

    browser.element('.modal-content').element('table').all('tr').all('td').even.should(
        have.exact_texts(
            'Aleksei Torsukov',
            'torsukov@gmail.com',
            'Male',
            '1234567890',
            '19 October,1911',
            'English, Computer Science',
            'Sports',
            'pic.jpg',
            'Robert Robertson, 1234 NW Bobcat Lane, St. Robert, MO 65584-5678',
            'NCR Delhi',
        )
    )
