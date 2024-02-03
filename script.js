import { initializeApp } from 'firebase/app';

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBcTEEZ9ALC-VxgPRApnZICMqaTyGjuXY8",
  authDomain: "scotty-s.firebaseapp.com",
  projectId: "scotty-s",
  storageBucket: "scotty-s.appspot.com",
  messagingSenderId: "233427453700",
  appId: "1:233427453700:web:086a69951fe49aa8227251",
  measurementId: "G-1YB0CSS9L9"
};

const app = initializeApp(firebaseConfig);

// Initialize Firebase
const analytics = getAnalytics(app);
const db = getFirestore(app);

// Get a list of cities from your database
const storage = firebase.storage();

function uploadVideo() {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];

  if (file) {
    // Create a storage reference from our storage service
    const storageRef = storage.ref();

    // Create a child reference
    const videosRef = storageRef.child('videos/' + file.name);

    // Upload the file
    videosRef.put(file).then((snapshot) => {
      console.log('Uploaded a blob or file!');
      alert('Video uploaded successfully!');
    }).catch((error) => {
      console.error('Failed to upload video:', error);
      alert('Failed to upload video. Please try again.');
    });
  } else {
    alert('Please select a video file.');
  }
}




      