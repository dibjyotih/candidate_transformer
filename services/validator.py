from email_validator import validate_email, EmailNotValidError
import phonenumbers

from models.candidate import Candidate

class Validator:
    @staticmethod
    def validate(candidate: Candidate):

        valid_emails = []

        for email in candidate.emails:
            try:
                validate_email(email, check_deliverability=False)
                valid_emails.append(email)
            except EmailNotValidError:
                pass

        candidate.emails = valid_emails

        valid_phones = []

        for phone in candidate.phones:
            try:
                number = phonenumbers.parse(phone, "IN")

                if phonenumbers.is_valid_number(number):
                    valid_phones.append(phone)

            except:
                pass

        candidate.phones = valid_phones

        return candidate