# Create a branch to save status or configuration
## Create a new branch
git branch test_branch

## Checkout the branch
git checkout test_branch

## Modify and commit a file
vi some_file.md
git commit -am 'Modified initial setup'

## Push branch to github
git push -u origin test_branch

## Switch back to Master
git checkout master


# Clone and checkout previous branch
git clone https://github.com/hughy603/example_project.git
cd example_project/
git checkout test_branch
