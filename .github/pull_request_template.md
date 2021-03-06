See CONTRIBUTING.md for contributor guidelines. 

Pull Request Checklist
 - [ ] Pull request is either from WIP to master or from some other branch to WIP.
 - [ ] Pull request includes a description of the change and the reason behind it.
 - [ ] Pull request includes unit tests for any new functionality. 
 - [ ] `pytest` passes locally.
 - [ ] `black creevey tests --skip-string-normalization` has been used to format the code.
 - [ ] `flake8 creevey tests` passes locally.
 - [ ] CHANGELOG has been updated.
 - [ ] Version in `_version.py` has been updated.
 - [ ] README and docs have been updated (if applicable).
