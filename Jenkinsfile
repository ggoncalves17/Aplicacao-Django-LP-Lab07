pipeline {
    agent any

    stages {
        stage('Listar Variáveis de Ambiente') {
            steps {
                bat 'set'
            }
        }
        stage('Verificar Python e pip') {
            steps {
                bat '''
                    python --version
                    pip --version
                '''
            }
        }
        stage('Clonar Repositório') {
            steps {
                git branch: 'main', url: 'https://github.com/ggoncalves17/Aplicacao-Django-LP-Lab07.git'
            }
        }
        stage('Configurar Ambiente') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Migrações da Base de Dados') {
            steps {
                bat 'python manage.py migrate --noinput'
            }
        }
        stage('Executar Testes') {
            steps {
                bat '''
                    python -m pytest --junitxml=results.xml topics_app/tests.py
                '''
            }
        }
        stage('Gerar Relatórios de Cobertura') {
            steps {
                bat '''
                    coverage html -d htmlcov
                '''
            }
        }
    }

    post {
        always {
            junit 'results.xml'
            archiveArtifacts artifacts: '**/results.xml', allowEmptyArchive: true
        }
        failure {
            echo 'Build falhou!'
        }
    }
}