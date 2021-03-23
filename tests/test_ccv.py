import unittest

from codecov_validator import ccv


class CcvTest(unittest.TestCase):
    def test_passing(self):
        self.assertEqual(1, 1)

    def test_valid_file(self):
        """
        Test valid example file from
        [documentation](https://docs.codecov.io/docs/codecovyml-reference).
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
        received = ccv.run_request(valid_file)
        self.assertIn("Valid!", received)

    def test_invalid_file(self):
        valid_file = """
codecovs:
  token: "<some token here>"
  bot: "codecov-io"
        """
        received = ccv.run_request(valid_file)
        self.assertIn("Wrong key", received)

    def test_ccv(self):
        wrong_filename = "wrong_codecov.yml"
        answer = "0"
        received = ccv.open_file(wrong_filename)
        self.assertEqual(answer, received)

    def test_check_valid_valid(self):
        valid_input = "Valid!"
        self.assertEqual(0, ccv.check_valid(valid_input))

    def test_check_valid_invalid(self):
        invalid_input = "Invalid!"
        self.assertEqual(1, ccv.check_valid(invalid_input))


if __name__ == "__main__":
    unittest.main()
