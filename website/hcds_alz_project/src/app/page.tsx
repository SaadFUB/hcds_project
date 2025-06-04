'use client'

import Sidebar from "hcds/components/Sidebar";
import InProgressPages from "hcds/pages/InProgressPages";
export default function Home() {
  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar />
      
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* <Header /> */}
        
        <main className="flex-1 overflow-y-auto p-6">
          {/* <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
            {metricsData.map((metric, index) => (
              <MetricCard key={index} {...metric} />
            ))}
          </div> */}
          
          <InProgressPages />
        </main>
      </div>
    </div>
  );
}
