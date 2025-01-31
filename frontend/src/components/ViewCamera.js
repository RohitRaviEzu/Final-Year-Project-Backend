import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles/ViewCamera.css"; // Add styles for horizontal grid layout

const ViewCamera = () => {
  const [cameras, setCameras] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/get-cameras/")
      .then((response) => {
        if (response.data.cameras) {
          setCameras(response.data.cameras); // Use the correct response format
        } else {
          setCameras(response.data); // Handle direct array response
        }
      })
      .catch((error) => {
        console.error("Error fetching cameras:", error);
      });
  }, []);

  return (
    <div className="view-camera-container">
      <h2>Available Cameras</h2>
      {cameras.length === 0 ? (
        <p>No cameras available.</p>
      ) : (
        <div className="camera-row">
          {cameras.map((camera, index) => (
            <div key={index} className="camera-card">
              <div className="camera-icon">📷</div>
              <h3>{camera.camera_name}</h3>
              <p>📍 {camera.location}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ViewCamera;
