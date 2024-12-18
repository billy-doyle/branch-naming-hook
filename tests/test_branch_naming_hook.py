import unittest
from io import StringIO
from unittest.mock import patch

from branch_naming_hook import validate_branch_name


class TestValidateBranchName(unittest.TestCase):
    @patch("branch_validator.Repo")
    def test_valid_branch_name(self, mock_repo):
        """Test that a valid branch name exits with status 0"""
        project_abbr = "PROJ"
        mock_repo.return_value.active_branch.name = "feat/PROJ-123-new-feature"

        with patch("sys.exit") as mock_exit:
            validate_branch_name(project_abbr)
            mock_exit.assert_called_once_with(0)

    @patch("branch_validator.Repo")
    def test_invalid_branch_name(self, mock_repo):
        """Test that an invalid branch name exits with status 1 and prints a message"""
        project_abbr = "PROJ"
        mock_repo.return_value.active_branch.name = "invalid-branch-name"

        with (
            patch("sys.exit") as mock_exit,
            patch("sys.stdout", new_callable=StringIO) as mock_stdout,
        ):
            validate_branch_name(project_abbr)
            mock_exit.assert_called_once_with(1)
            self.assertIn(
                "This branch violates the branch naming rules", mock_stdout.getvalue()
            )

    @patch("branch_validator.Repo")
    def test_main_branch_name(self, mock_repo):
        """Test that main branch names are valid"""
        project_abbr = "PROJ"
        for branch in ["master", "main", "develop"]:
            mock_repo.return_value.active_branch.name = branch
            with patch("sys.exit") as mock_exit:
                validate_branch_name(project_abbr)
                mock_exit.assert_called_once_with(0)

    @patch("branch_validator.Repo")
    def test_branch_name_with_special_characters(self, mock_repo):
        """Test valid branch names with special characters in the description"""
        project_abbr = "PROJ"
        mock_repo.return_value.active_branch.name = "fix/PROJ-456-fix-issue_v1.2"

        with patch("sys.exit") as mock_exit:
            validate_branch_name(project_abbr)
            mock_exit.assert_called_once_with(0)


if __name__ == "__main__":
    unittest.main()
