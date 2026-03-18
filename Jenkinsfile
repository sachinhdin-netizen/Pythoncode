pipeline (
}
agent any
stages (
stage('Checkout') {
steps (
git branch: 'main',
url: 'https://github.com/<your-username>/<your-repo>.git'
stage('Install Dependencies') (
steps (
pip3 install -r requirements.txt
}
stage('Run Tests') (
steps {
python3 -m unittest discover
}
)
stage('Package Application') {
steps (
zip -r app.zip.
}
}
stage('Deployment') (
steps {
}
echo "Deploy step customize for production!"
post [
success (echo "Build Successful!") failure (echo "Build Failed!")
}
}
