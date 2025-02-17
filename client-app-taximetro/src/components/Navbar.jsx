import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => (
  <nav className="bg-blue-500 p-4">
    <div className="container mx-auto flex flex-col md:flex-row justify-between items-center">
      <Link to="/" className="text-white text-xl font-bold mb-2 md:mb-0">App Taxímetro</Link>
      <div>
        <Link to="/configuracion" className="text-white mx-2">Configurar Tarifas</Link>
        <Link to="/historial" className="text-white mx-2">Historial</Link>
        <Link to="/estado" className="text-white mx-2">Estado</Link>
      </div>
    </div>
  </nav>
);

export default Navbar;
