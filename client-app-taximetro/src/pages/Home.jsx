import React from 'react';
import Taximeter from '../components/Taximeter';

const Home = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <main className="flex-grow container mx-auto p-4 text-center">
        <h1 className="text-4xl font-bold mb-4">Bienvenido a App Taxímetro</h1>
        <p className="text-lg mb-8">Gestiona y supervisa tus trayectos de manera eficiente.</p>
        <div className="flex justify-center space-x-4">
          <Taximeter />
        </div>
      </main>
    </div>
  );
};

export default Home;
