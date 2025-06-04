import { useState } from "react";
import { 
  ChevronRight, 
  Home, 
  Settings,
  Search,
  File,
  UsersRoundIcon,
} from "lucide-react";
import { cn } from "hcds/libs/utils";

const menuItems = [
  { icon: Home, label: "Overview", active: true, hasSubmenu: false },
  { icon: Settings, label: "Make a Prediction",},
  { icon: Search, label: "Explanation" },
  { icon: File, label: "About", },
  { icon: UsersRoundIcon, label: "Team", }
];

const Sidebar = () => {
  const [isCollapsed, setIsCollapsed] = useState(false);

  return (
    <div className={cn(
      "bg-white border-r border-gray-200 h-screen transition-all duration-300",
      isCollapsed ? "w-16" : "w-64"
    )}>
      <div className="p-6">
        <div className="flex items-center justify-between">
          <h1 className={cn(
            "text-xl font-bold text-blue-600 transition-opacity duration-300",
            isCollapsed && "opacity-0"
          )}>
            HCDS ALZ Project
          </h1>
          <button
            onClick={() => setIsCollapsed(!isCollapsed)}
            className="p-1 hover:bg-gray-100 rounded"
          >
            <ChevronRight className={cn(
              "w-4 h-4 transition-transform duration-300",
              isCollapsed && "rotate-180"
            )} />
          </button>
        </div>
      </div>
      
      <nav className="px-4 space-y-1">
        {menuItems.map((item, index) => (
          <div key={index} className="group">
            <div className={cn(
              "flex items-center justify-between px-3 py-2.5 rounded-lg cursor-pointer transition-colors",
              item.active 
                ? "bg-blue-50 text-blue-700" 
                : "text-gray-700 hover:bg-gray-50"
            )}>
              <div className="flex items-center space-x-3">
                <item.icon className="w-5 h-5" />
                {!isCollapsed && (
                  <span className="text-sm font-medium">{item.label}</span>
                )}
              </div>
              {!isCollapsed && item.hasSubmenu && (
                <ChevronRight className="w-4 h-4" />
              )}
            </div>
          </div>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;