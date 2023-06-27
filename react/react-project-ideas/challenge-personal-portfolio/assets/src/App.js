import React, { useEffect, useState } from "react";
import ArrowUpwardIcon from "@material-ui/icons/ArrowUpward";
import "./App.css";
import AboutPage from "./components/AboutPage";
import ContactPage from "./components/ContactPage";
import HomePage from "./components/HomePage";
import ProjectPage from "./components/ProjectPage";
import SkillPage from "./components/SkillPage";
import EducationPage from "./components/EducationPage";

export default function App() {

  // TODO: Complete the code here
  const toggleVisible = () => {

  };

  useEffect(() => {

  }, []);

  function scrollToTop() {

  }
  return (
    <>
      <div className="app-section" id="home">
        <HomePage />
      </div>
      <div className="app-section" id="about">
        <AboutPage />
      </div>
      <div className="app-section" id="skills">
        <SkillPage />
      </div>
      <div className="app-section" id="projects">
        <ProjectPage />
      </div>
      <div className="app-section">
        <EducationPage />
      </div>
      <div className="app-section-contact" id="contact">
        <ContactPage />
      </div>
      {showBackToTopBtn && (
        <button className="btn-back-to-top" onClick={scrollToTop}>
          <span> Back to Top</span>
          <ArrowUpwardIcon />
        </button>
      )}
    </>
  );
}
