// Taximeter.jsx
import React, { useState, useEffect, useRef } from 'react';
import {
    FaPlay,
    FaStop,
    FaUndo,
    FaPause,
    FaCarSide,
    FaClock,
    FaMoneyBillWave,
    FaHistory,
    FaCog
} from 'react-icons/fa';

const DEFAULT_CONFIG = {
    stopped_rate: 0.02,
    moving_rate: 0.05
};

const loadConfig = () => {
    return DEFAULT_CONFIG;
};

function Taximeter() {
    const [isRunning, setIsRunning] = useState(false);
    const [startTime, setStartTime] = useState(null);
    const [totalFare, setTotalFare] = useState(0.0);
    const [elapsedSeconds, setElapsedSeconds] = useState(0);
    const [isStopped, setIsStopped] = useState(false);
    const [stoppedRate, setStoppedRate] = useState(DEFAULT_CONFIG.stopped_rate);
    const [movingRate, setMovingRate] = useState(DEFAULT_CONFIG.moving_rate);

    const lastUpdateTimeRef = useRef(null);
    const frameId = useRef(null);

    const start = () => {
        if (!isRunning) {
            setIsRunning(true);
            const now = Date.now();
            setStartTime(now);
            lastUpdateTimeRef.current = now;
            setTotalFare(0.0);
            setElapsedSeconds(0);
            console.log("Taxímetro iniciado.");
        } else {
            console.warn("El taxímetro ya está en funcionamiento.");
        }
    };

    const stop = () => {
        if (isRunning) {
            setIsRunning(false);
            cancelAnimationFrame(frameId.current);
            console.log(`Taxímetro detenido. Tarifa total: ${totalFare.toFixed(2)}€`);
            saveHistory(totalFare);
        } else {
            console.warn("El taxímetro no está en funcionamiento.");
        }
    };

    const reset = () => {
        setIsRunning(false);
        cancelAnimationFrame(frameId.current);
        setStartTime(null);
        lastUpdateTimeRef.current = null;
        setTotalFare(0.0);
        setElapsedSeconds(0);
        setIsStopped(false);
        console.log("Taxímetro reiniciado.");
    };

    const toggleStopped = () => {
        setIsStopped(!isStopped);
    };

    const saveHistory = (fare) => {
        const now = new Date();
        const localTime = new Date(now.getTime() - (now.getTimezoneOffset() * 60000)).toISOString().slice(0, 19).replace("T", " ");
        const historyEntry = `Fecha y Hora: ${localTime}, Tarifa: ${fare.toFixed(2)}€\n`;
    
        let history = localStorage.getItem('taximeterHistory') || '';
        history += historyEntry;
        localStorage.setItem('taximeterHistory', history);
        console.log("Historial guardado:", historyEntry);
    };
    

    const updateRates = (newStoppedRate, newMovingRate) => {
        setStoppedRate(parseFloat(newStoppedRate));
        setMovingRate(parseFloat(newMovingRate));
        console.log(`Tasas actualizadas: Parado - ${newStoppedRate}€/s, En movimiento - ${newMovingRate}€/s`);
    };

    const updateFare = () => {
        const now = Date.now();
        const elapsedSinceLastUpdate = (now - lastUpdateTimeRef.current) / 1000; // Convertir a segundos

        if (elapsedSinceLastUpdate >= 1) {
            const secondsToAdd = Math.floor(elapsedSinceLastUpdate);
            setElapsedSeconds(prevSeconds => prevSeconds + secondsToAdd);

            setTotalFare(prevFare => {
                const newFare = prevFare + secondsToAdd * (isStopped ? stoppedRate : movingRate);
                return newFare;
            });

            lastUpdateTimeRef.current = now;
        }

        frameId.current = requestAnimationFrame(updateFare);
    };

    useEffect(() => {
        if (isRunning) {
            frameId.current = requestAnimationFrame(updateFare);
        } else {
            cancelAnimationFrame(frameId.current);
        }
        return () => cancelAnimationFrame(frameId.current);
    }, [isRunning, isStopped, stoppedRate, movingRate]);

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100 p-4 md:p-8 lg:p-16">
          <div className="w-100 max-w-xl bg-white rounded-2xl shadow-xl p-6 md:p-10 relative">
            <h1 className="text-3xl font-bold text-center text-gray-800 mb-4 flex items-center justify-center">
              <FaCarSide className="mr-2 text-gray-700" /> Taxímetro
            </h1>
            <p className="text-2xl font-semibold text-center text-gray-700 mb-4">
              <FaMoneyBillWave className="inline-block mr-1" />
              {totalFare.toFixed(2)}€
            </p>
      
            <div className="flex items-center justify-center mb-6">
              <FaClock className="mr-2 text-gray-500" />
              <span className="text-md text-gray-600">
                {elapsedSeconds}s
              </span>
              <span className="ml-4 text-md text-gray-600">
                ({isStopped ? 'Parado' : 'En Movimiento'})
              </span>
            </div>
      
            <div className="grid grid-cols-2 gap-4">
              <button
                className={`flex items-center justify-center bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded transition duration-300 ${isRunning ? 'opacity-50 cursor-not-allowed' : ''}`}
                onClick={start}
                disabled={isRunning}
              >
                <FaPlay className="mr-2" /> Iniciar
              </button>
              <button
                className={`flex items-center justify-center bg-red-600 hover:bg-red-700 text-white font-semibold py-2 px-4 rounded transition duration-300 ${!isRunning ? 'opacity-50 cursor-not-allowed' : ''}`}
                onClick={stop}
                disabled={!isRunning}
              >
                <FaStop className="mr-2" /> Detener
              </button>
              <button
                className="col-span-2 flex items-center justify-center bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-2 px-4 rounded transition duration-300"
                onClick={reset}
              >
                <FaUndo className="mr-2" /> Reiniciar
              </button>
              <button
                className={`col-span-2 flex items-center justify-center bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded transition duration-300 ${!isRunning ? 'opacity-50 cursor-not-allowed' : ''}`}
                onClick={toggleStopped}
                disabled={!isRunning}
              >
                {isStopped ? <><FaCarSide className="mr-2" /> Reanudar</> : <><FaPause className="mr-2" /> Parar</>}
              </button>
            </div>
      
            {/* Configuración */}
            <div className="mt-8">
              <h3 className="text-xl font-bold text-gray-800 mb-4">Actualizar Tasas de Cobro</h3>
              <label className="block text-md font-semibold text-gray-800 mb-2">
                Tarifa Parado (€/s):
                <input
                  type="number"
                  step="0.01"
                  value={stoppedRate}
                  onChange={(e) => setStoppedRate(parseFloat(e.target.value))}
                  className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-gray-500 sm:text-sm"
                />
              </label>
              <label className="block text-md font-semibold text-gray-800 mb-2">
                Tarifa En Movimiento (€/s):
                <input
                  type="number"
                  step="0.01"
                  value={movingRate}
                  onChange={(e) => setMovingRate(parseFloat(e.target.value))}
                  className="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-gray-500 focus:border-gray-500 sm:text-sm"
                />
              </label>
              <button
                className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-4 py-2 rounded mt-4 w-full transition duration-200"
                onClick={() => updateRates(stoppedRate, movingRate)}
              >
                Actualizar Tasas
              </button>
            </div>
      
            <div className="mt-8">
              <h3 className="text-xl font-bold text-gray-800 mb-4 flex items-center">
                <FaHistory className="mr-2 text-gray-600" /> Historial
              </h3>
              <div className="bg-gray-50 p-4 rounded-lg shadow-inner max-h-48 overflow-auto">
                <pre className="text-gray-700 text-sm">{localStorage.getItem('taximeterHistory') || 'No hay historial'}</pre>
              </div>
            </div>
          </div>
        </div>
      );
}

export default Taximeter;
