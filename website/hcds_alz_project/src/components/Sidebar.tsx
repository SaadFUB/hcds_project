import { useState } from "react";
import { 
  ChevronRight, 
  Home, 
  Settings,
  Search,
  File,
  UsersRoundIcon,
} from "lucide-react";

import { useLocation, Link } from "react-router-dom";

import { cn } from "hcds/libs/utils";

const menuItems = [
  { icon: Home, label: "Overview", active: true, hasSubmenu: false, path: "/"},
  { icon: Settings, label: "Make a Prediction", path: "/prediction"},
  { icon: Search, label: "Explanation", path: "/explanation"},
  { icon: File, label: "About", path: "/about"},
  { icon: UsersRoundIcon, label: "Team", path: "/team"},
];

const Sidebar = () => {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const location = useLocation();

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
          const isActive = item.path ? location.pathname === item.path : false;
          
          const content = (
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
              {!isCollapsed && item.hasSubmenu && (
                <ChevronRight className="w-4 h-4" />
              )}
            </div>
          );

          return (
            <div key={index} className="group">
              {item.path ? (
                <Link to={item.path}>
                  {content}
                </Link>
              ) : (
                content
              )}
            </div>
          );
        })}
      </nav>
    </div>
  );
};

export default Sidebar;