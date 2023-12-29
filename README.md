# Run with Docker
1. install Docker
2. Pull the Docker image:
```bash
docker pull mikhalkage/saucedemo:01
```
3. Run the Docker container interactively:
```bash
docker run -it mikhalkage/saucedemo:01
```

# GitHub Actions 
1. https://github.com/mikhalkaGE/RRS7_test_demo/actions
2. Select Actions workflow:
    - Run tests manual
    - Run tests manual with allure report
3. Run workflow (dropdown) from Branch: main
4. Observe GitHub page with Allure report:
    - by navigating: Repository Settings --> Pages --> Visit site
    - or directly https://mikhalkage.github.io/RRS7_test_demo/
    - TODO: history