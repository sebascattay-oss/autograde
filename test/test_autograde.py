import unittest
from unittest.mock import Mock, patch
from autograde import check_repo

class TestAutograde(unittest.TestCase):

    @patch('autograde.Github')
    def test_check_repo_success(self, mock_github_class):
        mock_repo = Mock()
        mock_github_class.return_value.get_repo.return_value = mock_repo

        mock_repo.get_branch.return_value = Mock()
        mock_repo.get_contents.return_value = Mock()

        result = check_repo("owner/repo")
        self.assertTrue(result)

    @patch('autograde.Github')
    def test_check_repo_no_main_branch(self, mock_github_class):
        mock_repo = Mock()
        mock_github_class.return_value.get_repo.return_value = mock_repo

        def side_effect(branch):
            if branch == 'main':
                raise Exception("Branch not found")
            return Mock()

        mock_repo.get_branch.side_effect = side_effect
        mock_repo.get_contents.return_value = Mock()

        result = check_repo("owner/repo")
        self.assertFalse(result)

    @patch('autograde.Github')
    def test_check_repo_no_feature_branch(self, mock_github_class):
        mock_repo = Mock()
        mock_github_class.return_value.get_repo.return_value = mock_repo

        def side_effect(branch):
            if branch == 'feature':
                raise Exception("Branch not found")
            return Mock()

        mock_repo.get_branch.side_effect = side_effect
        mock_repo.get_contents.return_value = Mock()

        result = check_repo("owner/repo")
        self.assertFalse(result)

    @patch('autograde.Github')
    def test_check_repo_no_file(self, mock_github_class):
        mock_repo = Mock()
        mock_github_class.return_value.get_repo.return_value = mock_repo

        mock_repo.get_branch.return_value = Mock()
        mock_repo.get_contents.side_effect = Exception("File not found")

        result = check_repo("owner/repo")
        self.assertFalse(result)

    @patch('autograde.Github')
    def test_check_repo_invalid_repo(self, mock_github_class):
        mock_github_class.return_value.get_repo.side_effect = Exception("Repository not found")

        result = check_repo("invalid/repo")
        self.assertFalse(result)

    @patch('autograde.Github')
    def test_check_repo_multiple_failures(self, mock_github_class):
        mock_repo = Mock()
        mock_github_class.return_value.get_repo.return_value = mock_repo

        def side_effect(branch):
            raise Exception("Branch not found")

        mock_repo.get_branch.side_effect = side_effect
        mock_repo.get_contents.side_effect = Exception("File not found")

        result = check_repo("owner/repo")
        self.assertFalse(result)