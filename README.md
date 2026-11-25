# ICT Lab 6 — Serverless Function and CI/CD

## Project

This project implements a simple serverless function with:

- GET /time
- POST /echo
- 400 error handling
- 404 error handling
- automated pytest tests
- GitHub Actions CI/CD

## Tests

![Tests](screenshots/01_pytest.jpg)

## Local Run

### Time

![Time](screenshots/02_time.jpg)

### Echo

![Echo](screenshots/03_echo.jpg)

### 400 Error

![400](screenshots/04_error_400.jpg)

### 404 Error

![404](screenshots/05_error_404.jpg)

## CI/CD

### Successful Pipeline

![Green pipeline](screenshots/06_actions_green.jpg)

### Failed Pipeline

![Red pipeline](screenshots/07_actions_red.jpg)

### Fixed Pipeline

![Green pipeline](screenshots/08_actions_green_fixed.jpg)

### Artifact

![Artifact](screenshots/09_artifact.jpg)

## Conclusion

The function was tested locally and automatically with pytest.

GitHub Actions runs the tests on every push.

The Lambda package is created only when all tests pass.