from playwright.sync_api import sync_playwright

class DeleteApi:
    def delete_account(self, email, password):
        with sync_playwright() as p:
            api_context = p.request.new_context(
                base_url="https://automationexercise.com"
            )
            payload = {
                "email": email,
                "password": password
            }

            response = api_context.delete(
                "/api/deleteAccount",
                form=payload
            )

            print(response.status)
            print(response.text())
