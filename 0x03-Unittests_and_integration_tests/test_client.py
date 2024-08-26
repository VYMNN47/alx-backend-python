#!/usr/bin/env python3
"""Module for Unitttesting client.py"""
import unittest
from unittest.mock import MagicMock, patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing the GithubOrgClient Class"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"key": "value"})
    def test_org(self, org, mock_get_json):
        """Test for GithubOrgClient.org method"""
        client = GithubOrgClient(org)
        result = client.org

        self.assertEqual(result, {"key": "value"})
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Test for GithubOrgClient._public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "mocked_url"}
            client = GithubOrgClient("org")
            result = client._public_repos_url
            self.assertEqual(result, "mocked_url")

    @patch('client.get_json', return_value=[{"name": "value1"},
                                            {"name": "value2"}])
    def test_public_repos(self, mocked_get_json):
        """Test for GithubOrgClient._public_repos method"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "mock_url"
            client = GithubOrgClient('org')
            result = client.public_repos()

            self.assertAlmostEqual(result, ['value1', 'value2'])
            mocked_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test for GithubOrgClient.has_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test Integration class to test GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Setup class for patching requests.get"""
        cls.get_patcher = patch('requests.get',
                                side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Teardown class for stopping patcher"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """Mocked requests.get to return payloads"""
        if url == "https://api.github.com/orgs/google":
            response = MagicMock()
            response.json.return_value = TEST_PAYLOAD[0][0]
            return response
        if url == "https://api.github.com/orgs/google/repos":
            response = MagicMock()
            response.json.return_value = TEST_PAYLOAD[0][1]
            return response
        return MagicMock()

    def test_public_repos(self):
        """Test for GithubOrgClient.public_repos"""
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos with license"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
