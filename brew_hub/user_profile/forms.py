from allauth.account.forms import SignupForm


class BrewHubSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["email"]

    class Meta:
        fields = [
            "username",
            "password1",
            "password2",
        ]
