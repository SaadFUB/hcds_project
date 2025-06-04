"use client";

import { Routes, Route } from "react-router-dom";
import { BrowserRouter } from 'react-router-dom';

import Sidebar from "hcds/components/Sidebar";
import OverviewPage from "hcds/pages/overview";
import PredictionPage from "hcds/pages/prediction";
import ExplanationPage from "hcds/pages/explanation";
import AboutPage from "hcds/pages/about";
import TeamPage from "hcds/pages/team";

export default function Home() {
  return (
    <BrowserRouter>
    <div className="flex h-screen bg-gray-50">
      <Sidebar />

      <div className="flex-1 flex flex-col overflow-hidden">
        {/* <Header /> */}

        <div className="flex-1 flex flex-col overflow-hidden">
          <main className="flex-1 overflow-y-auto p-6">
            <Routes>
              <Route path="/" element={<OverviewPage />} />
              <Route path="/prediction" element={<PredictionPage />} />
              <Route path="/explanation" element={<ExplanationPage />} />
              <Route path="/about" element={<AboutPage />} />
              <Route path="/team" element={<TeamPage />} />
            </Routes>
          </main>
        </div>
      </div>
    </div>
    </BrowserRouter>
  );
}
