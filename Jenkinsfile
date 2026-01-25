pipeline {
  agent any

  environment {
    APP_NAME = "flaskapp"
    IMAGE    = "flaskapp"
    PORT     = "5000"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Docker Build') {
      steps {
        sh '''
          GIT_SHA=$(git rev-parse --short HEAD)
          docker build -t ${IMAGE}:${GIT_SHA} .
          docker tag ${IMAGE}:${GIT_SHA} ${IMAGE}:latest
        '''
      }
    }

    stage('Run Container') {
      steps {
        sh '''
          docker rm -f ${APP_NAME} || true
          docker run -d --name ${APP_NAME} -p ${PORT}:${PORT} ${IMAGE}:latest
          docker ps
        '''
      }
    }
  }
}