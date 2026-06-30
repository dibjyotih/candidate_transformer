from email_validator import validate_email, EmailNotValidError
import phonenumbers

from models.candidate import Candidate


class Validator:

    @staticmethod
    def validate(candidate: Candidate) -> Candidate:
        """
        Validates candidate data.
        Removes invalid emails and phone numbers.
        """

        # -----------------------------
        # Validate Emails
        # -----------------------------

        valid_emails = []

        for email in candidate.personal.emails:

            try:
                validate_email(email, check_deliverability=False)
                valid_emails.append(email.lower().strip())

            except EmailNotValidError:
                pass

        candidate.personal.emails = list(set(valid_emails))

        # -----------------------------
        # Validate Phone Numbers
        # -----------------------------

        valid_numbers = []

        for phone in candidate.personal.phones:

            try:

                number = phonenumbers.parse(phone, "IN")

                if phonenumbers.is_valid_number(number):

                    formatted = phonenumbers.format_number(
                        number,
                        phonenumbers.PhoneNumberFormat.E164
                    )

                    valid_numbers.append(formatted)

            except Exception:
                continue

        candidate.personal.phones = list(set(valid_numbers))

        # -----------------------------
        # Remove Empty Skills
        # -----------------------------

        candidate.professional.skills = [

            skill.strip()

            for skill in candidate.professional.skills

            if skill.strip()

        ]

        # -----------------------------
        # Remove Duplicate Skills
        # -----------------------------

        candidate.professional.skills = sorted(

            list(

                set(candidate.professional.skills)

            )

        )

        return candidate