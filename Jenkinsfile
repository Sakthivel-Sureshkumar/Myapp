pipeline {
    agent any

    environment {
        IMAGE_NAME = "sakthivel121204/flask-app"
    }

    stages {

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Docker Push') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop flask-container || true
                docker rm flask-container || true
                docker pull $IMAGE_NAME
                docker run -d -p 5000:5000 --name flask-container $IMAGE_NAME
                '''
            }
        }
    }
}