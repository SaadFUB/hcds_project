import React, { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeHighlight from "rehype-highlight";
import "highlight.js/styles/github.css";
import "./github-markdown.css";
import Layout from "hcds/components/Layout";

const url =
  "https://raw.githubusercontent.com/SaadFUB/hcds_project/refs/heads/main/metadata.md";

const AboutPage = () => {
  const [markdown, setMarkdown] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMarkdown = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const text = await response.text();
        setMarkdown(text);
      } catch (err) {
        if (err instanceof Error) {
          setError(`Failed to load markdown: ${err.message}`);
        } else {
          setError(`Failed to load markdown: Unknown error`);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchMarkdown();
  }, []);

  if (loading) {
    return (
      <Layout>
        <div className="flex justify-center items-center min-h-64">
          <div className="text-gray-600">Loading markdown content...</div>
        </div>
      </Layout>
    );
  }

  if (error) {
    return (
      <Layout>
        <div className="max-w-4xl mx-auto p-6">
          <div className="bg-red-50 border border-red-200 rounded p-4">
            <p className="text-red-700 font-medium">Error Loading Content</p>
            <p className="text-red-600 text-sm mt-1">{error}</p>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="max-w-4xl mx-auto p-6">
        <div className="bg-white border border-gray-200 rounded-lg p-8">
          <div className="github-markdown">
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              rehypePlugins={[rehypeHighlight]}
            >
              {markdown}
            </ReactMarkdown>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default AboutPage;
