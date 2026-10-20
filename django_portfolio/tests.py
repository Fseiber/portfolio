import os
import runpy
from pathlib import Path
from unittest.mock import patch

from django.core.exceptions import DisallowedHost
from django.test import RequestFactory, SimpleTestCase, override_settings


class DeploymentHostsTests(SimpleTestCase):
    def test_vercel_domains_are_accepted_and_other_domains_rejected(self):
        environment = {
            "ALLOWED_HOSTS": "localhost, custom.example.com",
            "VERCEL_URL": "portfolio-preview.vercel.app",
            "VERCEL_PROJECT_PRODUCTION_URL": "portfolio-production.vercel.app",
        }
        with patch.dict(os.environ, environment):
            configuration = runpy.run_path(str(Path(__file__).with_name("settings.py")))
        with override_settings(DEBUG=False, ALLOWED_HOSTS=configuration["ALLOWED_HOSTS"]):
            factory = RequestFactory()
            for host in ("localhost", "custom.example.com", "portfolio-preview.vercel.app", "portfolio-production.vercel.app"):
                self.assertEqual(factory.get("/", HTTP_HOST=host).get_host(), host)
            with self.assertRaises(DisallowedHost):
                factory.get("/", HTTP_HOST="untrusted.example.com").get_host()
