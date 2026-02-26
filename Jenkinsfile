// pipeline {
//   agent any

//   environment {
//     APP_NAME = "flaskapp"
//     IMAGE    = "flaskapp"
//     PORT     = "5000"
//   }

//   stages {

//     stage('Checkout') {
//       steps {
//         checkout scm
//       }
//     }

//     stage('Build Docker Image') {
//       steps {
//         sh '''
//           echo "Cleaning old docker images..."
//           docker system prune -af || true

//           echo "Building fresh image..."
//           docker build -t ${IMAGE}:latest .
//         '''
//       }
//     }

//     stage('Deploy Container') {
//       steps {
//         sh '''
//           docker rm -f ${APP_NAME} || true
//           docker run -d --name ${APP_NAME} -p ${PORT}:${PORT} ${IMAGE}:latest
//         '''
//       }
//     }

//     stage('Verify') {
//       steps {
//         sh 'docker ps'
//       }
//     }
//   }
// }
pipeline {
    agent any

    environment {
        IMAGE_NAME = "sakthivel121204/flask-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https:/Sakthivel-Sureshkumar/github.com/Sakthivel-Sureshkumar/Myapp.git'
            }
        }

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