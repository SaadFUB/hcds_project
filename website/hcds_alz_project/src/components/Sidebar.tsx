"use client";

import { useState } from "react";
import { usePathname } from "next/navigation";
import {
  ChevronRight,
  Home,
  Settings,
  Search,
  File,
  UsersRoundIcon,
} from "lucide-react";
import { cn } from "hcds/libs/utils";
import Link from "next/link";

const menuItems = [
  { icon: Home, label: "Overview", path: "/" },
  { icon: Settings, label: "Make a Prediction", path: "/prediction" },
  { icon: Search, label: "Explanation", path: "/explanation" },
  { icon: File, label: "About", path: "/about" },
  { icon: UsersRoundIcon, label: "Team", path: "/team" },
];

const Sidebar = () => {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const pathname = usePathname();

  return (
    <div className={cn(
      "bg-white border-r border-gray-200 h-screen transition-all duration-300 relative",
      isCollapsed ? "w-20" : "w-64"
    )}>
      <div className="p-6">
        <div className="flex items-center justify-between">
          <h1 className={cn(
            "text-xl font-bold text-blue-600 transition-opacity duration-300",
            isCollapsed && "opacity-0"
          )}>
            HCDS ALZ Project
          </h1>
        </div>
      </div>
     
      <button
        onClick={() => setIsCollapsed(!isCollapsed)}
        className={cn(
          "absolute top-6 p-1 hover:bg-gray-100 rounded transition-all duration-300 z-10",
          isCollapsed ? "right-2" : "right-6"
        )}
      >
        <ChevronRight className={cn(
          "w-4 h-4 transition-transform duration-300 text-gray-600",
          isCollapsed ? "rotate-0" : "rotate-180"
        )} />
      </button>
     
      <nav className="px-4 space-y-1 mt-4">
        {menuItems.map((item, index) => {
          const isActive = pathname === item.path;
         
          return (
            <div key={index} className="group">
              <Link href={item.path}>
                <div className={cn(
                  "flex items-center justify-between px-3 py-2.5 rounded-lg cursor-pointer transition-colors",
                  isActive
                    ? "bg-blue-50 text-blue-700"
                    : "text-gray-700 hover:bg-gray-50"
                )}>
                  <div className="flex items-center space-x-3">
                    <item.icon className="w-5 h-5 flex-shrink-0" />
                    {!isCollapsed && (
                      <span className="text-sm font-medium">{item.label}</span>
                    )}
                  </div>
                </div>
              </Link>
            </div>
          );
        })}
      </nav>
    </div>
  );
};

export default Sidebar;