# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

# [1.2.0] - 2019-03-07
### Added
- Added hosted docs for readthedocs.

# [1.1.0] - 2019-03-02
### Added
- `Pipeline` runs return "run reports"
- `CustomReportingPipeline` class allows custom run report fields

# [1.0.0] - 2019-02-23
### Changed
- Redesigned library around `Pipeline` abstraction

# [0.3.2] - 2019-02-15
### Changed
- Switched to using one requests session in each download thread.

# [0.3.1] - 2019-01-29
### Added
- Added boto3 to setup.py requirements.

# [0.3.0] - 2019-01-29
### Added
- Added dataset module

# [0.2.0] - 2019-01-26
### Changed
- Elevated `group_train_test_split` to a public function in its own module.

# [0.1.15] - 2019-01-22
### Changed
- Use `black` to format code.

# [0.1.11] - 2019-01-17
### Fixed
- Address flake8 complaints.

# [0.1.10] - 2019-01-17
### Changed
- Used black to format code.
- Remove download instructions from README now that a simple pip install should work.

# [0.1.9] - 2019-01-17
### Added
- Added functionality to save_response_content_as_png() to allow resize on download

# [0.1.8] - 2019-01-17
### Added
- Fill in some missing type hints.

# [0.1.5] - 2019-01-17
### Added
- Modify Jenkins job to avoid trying to push old versions to PyPI.

# [0.1.3] - 2019-01-15
### Fixed
- Catch `FileExistsError` in case in which another thread creates directory after we check for it.

# [0.1.2] - 2019-01-11
### Fixed
- Configure PyPI Markdown rendering.

# [0.1.0] - 2019-01-07
### Added
- Functions for downloading, resizing, and creating imagenet-style symlinks.
- Basic docs.
