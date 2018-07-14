import random

from ansible.plugins.vars import BaseVarsPlugin

class VarsModule(BaseVarsPlugin):
    def get_vars(self, loader, path, entities):
        return {'django_secret_key':''.join([random.SystemRandom().choice(
                'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
            for i in range(50)])}

