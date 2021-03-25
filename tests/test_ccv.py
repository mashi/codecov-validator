import unittest

from click.testing import CliRunner

from codecov_validator import ccv

invalid_file = """
codecovs:
token: "<some token here>"
bot: "codecov-io"
"""


valid_file = """
codecov:
  token: "<some token here>"
  bot: "codecov-io"
  ci:
    - "travis.org"
  strict_yaml_branch: "yaml-config"
  max_report_age: 24
  disable_default_path_fixes: no
  require_ci_to_pass: yes
  notify:
    after_n_builds: 2
    wait_for_ci: yes
"""


class CcvTest(unittest.TestCase):
    def test_passing(self):
        self.assertEqual(1, 1)

    def test_valid_file(self):
        """
        Test valid example file from
        [documentation](https://docs.codecov.io/docs/codecovyml-reference).
        """
        received = ccv.run_request(valid_file)
        self.assertIn("Valid!", received)

    def test_invalid_file(self):
        received = ccv.run_request(invalid_file)
        self.assertIn("Wrong key", received)

    def test_open_file_wrong_filename(self):
        wrong_filename = "wrong_codecov.yml"
        with self.assertRaises(SystemExit) as cm:
            received = ccv.open_file(wrong_filename)
        self.assertEqual(cm.exception.code, 1)

    def test_open_file_valid_filename(self):
        right_filename = "codecov.yml"
        received = ccv.open_file(right_filename)
        self.assertIs(type(received), bytes)

    def test_check_valid_valid_input(self):
        valid_input = "Valid!"
        with self.assertRaises(SystemExit) as cm:
            ccv.check_valid(valid_input)
        self.assertEqual(cm.exception.code, 0)
        self.assertNotEqual(cm.exception.code, 1)

    def test_check_valid_invalid_input(self):
        invalid_input = "Invalid!"
        with self.assertRaises(SystemExit) as cm:
            ccv.check_valid(invalid_input)
        self.assertEqual(cm.exception.code, 1)
        self.assertNotEqual(cm.exception.code, 0)

    def test_ccv_valid_clirunner(self):
        runner = CliRunner()
        result = runner.invoke(ccv.ccv)
        self.assertEqual(result.exit_code, 0)


if __name__ == "__main__":
    unittest.main()
