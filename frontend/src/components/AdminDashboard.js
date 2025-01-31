import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import AddCamera from "./AddCamera"; // Import AddCamera component
import "../styles/AdminDashboard.css";

const AdminDashboard = () => {
  const [admin, setAdmin] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const storedAdmin = localStorage.getItem("admin");
    if (storedAdmin) {
      setAdmin(JSON.parse(storedAdmin));
    } else {
      navigate("/login");
    }
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem("admin");
    navigate("/login");
  };

  return (
    <div className="dashboard-container">
      {/* Sidebar */}
      <div className="sidebar">
        <h3>Admin Panel</h3>
        <button onClick={() => setShowForm(true)}>Add Camera</button>
        <button onClick={() => navigate("/view-camera")}>View Camera</button>
        <button onClick={() => navigate("/detection-logs")}>
          Detection Logs
        </button>
        <button onClick={handleLogout}>Logout</button>
      </div>

      {/* Main Content */}
      <div className="content">
        <h2>Welcome, {admin?.email}</h2>
        <p>This is your admin dashboard.</p>

        {/* Show AddCamera component when clicking "Add Camera" */}
        {showForm && <AddCamera onClose={() => setShowForm(false)} />}
      </div>
    </div>
  );
};

export default AdminDashboard;
