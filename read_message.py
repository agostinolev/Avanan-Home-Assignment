import re


class DataLossPrevention:
    EXPRESSION_FOR_BANK_ACCOUNT_NUMBER = "^\d{9,18}$"
    EXPRESSION_FOR_CREDIT_CARD_NUMBER = "^[1-9][0-9]{3}(-[0-9]{4}){3}$"
    EXPRESSIONS_TO_CHECK = {
        "banck_account_number": EXPRESSION_FOR_BANK_ACCOUNT_NUMBER,
        "credit_card_number": EXPRESSION_FOR_CREDIT_CARD_NUMBER,
    }

    def find_leak_in_file(filepath: str) -> None:
        with open(filepath, "r") as f:
            messages = f.readlines()
        messages_and_patterns_found = []
        for message in messages:
            message_and_pattern_found = self._read_message(message=message)
            if message_and_pattern_found:
                message_and_pattern_found.extend((message_and_pattern_found[0],message_and_pattern_found[1]))
        
        for message, pattern_found in message_and_pattern_found:
            print(f"Leak in file and messages found. Message {message} with pattern {pattern_found}")

    def _read_message(message: str) -> tuple[str, str] | None:
        for expression_to_check in self.EXPRESSIONS_TO_CHECK:
            pattern_found = re.findall(expression_to_check, message)
            if re.findall(expression_to_check, message):
                return message, pattern_found[0]
        return None        
