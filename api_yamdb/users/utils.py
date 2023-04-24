from django.core.mail import send_mail

from api_yamdb.settings import EMAIL_FROM


class Util:
    @staticmethod
    def send_confirmation_code(data):
        """Oтправляем на почту подтверждения."""

        send_mail(subject="Код подтверждения",
                  message=("Отправте ваш код подтверждения: \n"
                           f"{data['confirmation_code']} \n"
                           "на эндпоинт /api/v1/auth/token/ "
                           "в следующем формате\n"
                           "{\n"
                           f"\t\"username\": \"{data['username']}\",\n"
                           "\t\"confirmation_code\": "
                           f"\"{data['confirmation_code']}\"\n"
                           "}\n"),
                  from_email=EMAIL_FROM,
                  recipient_list=(data['email'],),
                  fail_silently=False,)
