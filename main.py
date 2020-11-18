from docx import Document

document = Document()

name = input('What is your name? ')
phone_number = input(' What is your phone number? ')
email = input('What is your email address? ')

document.add_paragraph(
    name + ' | ' + phone_number + ' | ' + email
)

document.save("cv.docx")
