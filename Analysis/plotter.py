#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

class Data():
    
    def reading_the_data():
        
        Meroli_Experiment = np.loadtxt('exp_Meroli_100MeV_electron_5p6um_Si.dat')
        Meroli_Simulation = np.loadtxt('Hist_Edep.dat')
        Edep = np.genfromtxt('Edep.csv')
        
        Edep_Si = np.genfromtxt('Edep_Si.csv')
        Edep_Pb = np.genfromtxt('Edep_Pb.csv')
        Edep_Cu = np.genfromtxt('Edep_Cu.csv')
        Edep_Au = np.genfromtxt('Edep_Au.csv')
        Edep_Ag = np.genfromtxt('Edep_Ag.csv')
        
        Edep_Si_2_5_um = np.genfromtxt('Edep_Si_2_5_um.csv')
        Edep_Si_5_6_um = np.genfromtxt('Edep_Si_5_6_um.csv')
        Edep_Si_15_um = np.genfromtxt('Edep_Si_15_um.csv')
        Edep_Si_30_um = np.genfromtxt('Edep_Si_30_um.csv')
        Edep_Si_50_um = np.genfromtxt('Edep_Si_50_um.csv')
        Edep_Si_100_um = np.genfromtxt('Edep_Si_100_um.csv')
        
        Edep_mu = np.genfromtxt('Edep_mu.csv')
        Edep_tau = np.genfromtxt('Edep_tau.csv')
        
        return Meroli_Experiment, Meroli_Simulation, Edep, Edep_Si, Edep_Pb, Edep_Cu, Edep_Si_2_5_um, Edep_Si_5_6_um, Edep_Si_15_um, Edep_Si_30_um, Edep_Si_50_um, Edep_Si_100_um, Edep_mu, Edep_tau, Edep_Au, Edep_Ag

class Plots():
    
    def comparing_meroli_experiment_meroli_simulation():
        
        Meroli_Experiment, Meroli_Simulation, Edep, Edep_Si, Edep_Pb, Edep_Cu, Edep_Si_2_5_um, Edep_Si_5_6_um, Edep_Si_15_um, Edep_Si_30_um, Edep_Si_50_um, Edep_Si_100_um, Edep_mu, Edep_tau, Edep_Au, Edep_Ag = Data.reading_the_data()
        
        normalization_factor = np.max(Meroli_Experiment[:,1])/np.max(Meroli_Simulation[:,2])
        scale_to_kev = 1000
        
        plt.scatter(Meroli_Experiment[:,0], Meroli_Experiment[:,1], s = 2, color = 'b', marker='o', label = 'Meroli Experiment')
        plt.plot(Meroli_Simulation[:,1]*scale_to_kev, Meroli_Simulation[:,2]*normalization_factor, color = 'r', label = 'Meroli Simulation')
        
        plt.legend()
        plt.title('Si')
        plt.xlabel('Energy loss (KeV)')
        plt.ylabel('Energy loss distribution (arb. units)')
        plt.show()
    
    def comparing_meroli_experiment_g4simulation():
        
        Meroli_Experiment, Meroli_Simulation, Edep, Edep_Si, Edep_Pb, Edep_Cu, Edep_Si_2_5_um, Edep_Si_5_6_um, Edep_Si_15_um, Edep_Si_30_um, Edep_Si_50_um, Edep_Si_100_um, Edep_mu, Edep_tau, Edep_Au, Edep_Ag = Data.reading_the_data()
        
        normalization_factor = np.max(Meroli_Experiment[:,1])/np.max(Edep[:,2])
        scale_to_kev = 1000
        
        plt.scatter(Meroli_Experiment[:,0], Meroli_Experiment[:,1], s = 2, color = 'b', marker='o', label = 'Meroli Experiment')
        plt.plot(Edep[:,1]*scale_to_kev, Edep[:,2]*normalization_factor, color = 'r', label = 'Geant4 Simulation')
        
        plt.legend()
        plt.title('Si')
        plt.xlabel('Energy loss (KeV)')
        plt.ylabel('Energy loss distribution (arb. units)')
        plt.show()
    
    def comparing_meroli_simulation_g4simulation():

        Meroli_Experiment, Meroli_Simulation, Edep, Edep_Si, Edep_Pb, Edep_Cu, Edep_Si_2_5_um, Edep_Si_5_6_um, Edep_Si_15_um, Edep_Si_30_um, Edep_Si_50_um, Edep_Si_100_um, Edep_mu, Edep_tau, Edep_Au, Edep_Ag = Data.reading_the_data()
        
        normalization_factor = np.max(Meroli_Simulation[:,2])/np.max(Edep[:,2])
        scale_to_kev = 1000
        
        plt.scatter(Meroli_Simulation[:,1]*scale_to_kev, Meroli_Simulation[:,2], s = 2, color = 'g', marker='x', label = 'Meroli Simulation')
        plt.plot(Edep[:,1]*scale_to_kev, Edep[:,2]*normalization_factor, color = 'r', label = 'Geant4 Simulation')
                
        plt.legend()
        plt.title('Si')
        plt.xlabel('Energy loss (KeV)')
        plt.ylabel('Energy loss distribution (arb. units)')
        plt.show()

    def comparing_g4_simulation_materials():

        Meroli_Experiment, Meroli_Simulation, Edep, Edep_Si, Edep_Pb, Edep_Cu, Edep_Si_2_5_um, Edep_Si_5_6_um, Edep_Si_15_um, Edep_Si_30_um, Edep_Si_50_um, Edep_Si_100_um, Edep_mu, Edep_tau, Edep_Au, Edep_Ag = Data.reading_the_data()
        
        scale_to_kev = 1000
        
        plt.plot(Edep_Si[:,1]*scale_to_kev, ((Edep_Si[:,2]) - np.min(Edep_Si[:,2]))/(np.max(Edep_Si[:,2]) - np.min(Edep_Si[:,2])), color = 'b', label = 'Silicon')
        plt.plot(Edep_Pb[:,1]*scale_to_kev, ((Edep_Pb[:,2]) - np.min(Edep_Pb[:,2]))/(np.max(Edep_Pb[:,2]) - np.min(Edep_Pb[:,2])), color = 'r', label = 'Lead')
        plt.plot(Edep_Cu[:,1]*scale_to_kev, ((Edep_Cu[:,2]) - np.min(Edep_Cu[:,2]))/(np.max(Edep_Cu[:,2]) - np.min(Edep_Cu[:,2])), color = 'g', label = 'Cooper')
        plt.plot(Edep_Au[:,1]*scale_to_kev, ((Edep_Au[:,2]) - np.min(Edep_Au[:,2]))/(np.max(Edep_Au[:,2]) - np.min(Edep_Au[:,2])), color = 'k', label = 'Gold')
        plt.plot(Edep_Ag[:,1]*scale_to_kev, ((Edep_Ag[:,2]) - np.min(Edep_Ag[:,2]))/(np.max(Edep_Ag[:,2]) - np.min(Edep_Ag[:,2])), color = 'm', label = 'Silver')
                
        plt.legend()
        plt.xlabel('Energy loss (KeV)')
        plt.ylabel('Energy loss distribution (arb. units)')
        plt.show()

    def comparing_g4_simulation_thicknesses():

        Meroli_Experiment, Meroli_Simulation, Edep, Edep_Si, Edep_Pb, Edep_Cu, Edep_Si_2_5_um, Edep_Si_5_6_um, Edep_Si_15_um, Edep_Si_30_um, Edep_Si_50_um, Edep_Si_100_um, Edep_mu, Edep_tau, Edep_Au, Edep_Ag = Data.reading_the_data()
        
        scale_to_kev = 1000
        
        plt.plot(Edep_Si_2_5_um[:,1]*scale_to_kev, ((Edep_Si_2_5_um[:,2]) - np.min(Edep_Si_2_5_um[:,2]))/(np.max(Edep_Si_2_5_um[:,2]) - np.min(Edep_Si_2_5_um[:,2])), color = 'c', label = '2.5 um')
        plt.plot(Edep_Si_5_6_um[:,1]*scale_to_kev, ((Edep_Si_5_6_um[:,2]) - np.min(Edep_Si_5_6_um[:,2]))/(np.max(Edep_Si_5_6_um[:,2]) - np.min(Edep_Si_5_6_um[:,2])), color = 'b', label = '5.6 um')
        plt.plot(Edep_Si_15_um[:,1]*scale_to_kev,((Edep_Si_15_um[:,2]) - np.min(Edep_Si_15_um[:,2]))/(np.max(Edep_Si_15_um[:,2]) - np.min(Edep_Si_15_um[:,2])), color = 'r', label = '15 um')
        plt.plot(Edep_Si_30_um[:,1]*scale_to_kev, ((Edep_Si_30_um[:,2]) - np.min(Edep_Si_30_um[:,2]))/(np.max(Edep_Si_30_um[:,2]) - np.min(Edep_Si_30_um[:,2])), color = 'g', label = '30 um')
        plt.plot(Edep_Si_50_um[:,1]*scale_to_kev, ((Edep_Si_50_um[:,2]) - np.min(Edep_Si_50_um[:,2]))/(np.max(Edep_Si_50_um[:,2]) - np.min(Edep_Si_50_um[:,2])), color = 'm', label = '50 um')
        plt.plot(Edep_Si_100_um[:,1]*scale_to_kev, ((Edep_Si_100_um[:,2]) - np.min(Edep_Si_100_um[:,2]))/(np.max(Edep_Si_100_um[:,2]) - np.min(Edep_Si_100_um[:,2])), color = 'k', label = '100 um')
        
        maxima = [np.max(Edep_Si_2_5_um[:,2]), np.max(Edep_Si_5_6_um[:,2]), np.max(Edep_Si_15_um[:,2]), np.max(Edep_Si_30_um[:,2]), np.max(Edep_Si_50_um[:,2]), np.max(Edep_Si_100_um[:,2])]
        thicknesses = [2.5, 5.6, 15, 30, 50, 100]
        
        plt.legend()
        plt.title('Si')
        plt.xlabel('Energy loss (KeV)')
        plt.ylabel('Energy loss distribution (arb. units)')
        plt.show()
        
        plt.plot(thicknesses, maxima, color = 'b', marker='x')
        plt.title('Si')
        plt.xlabel('Silicon (um)')
        plt.ylabel('Energy loss distribution (arb. units)')
        plt.show()
        
    def comparing_g4_simulation_particles():

        Meroli_Experiment, Meroli_Simulation, Edep, Edep_Si, Edep_Pb, Edep_Cu, Edep_Si_2_5_um, Edep_Si_5_6_um, Edep_Si_15_um, Edep_Si_30_um, Edep_Si_50_um, Edep_Si_100_um, Edep_mu, Edep_tau, Edep_Au, Edep_Ag = Data.reading_the_data()
        
        scale_to_kev = 1000
        
        plt.plot(Edep[:,1]*scale_to_kev, ((Edep[:,2]) - np.min(Edep[:,2]))/(np.max(Edep[:,2]) - np.min(Edep[:,2])), color = 'b', label = 'e-')
        plt.plot(Edep_mu[:,1]*scale_to_kev, ((Edep_mu[:,2]) - np.min(Edep_mu[:,2]))/(np.max(Edep_mu[:,2]) - np.min(Edep_mu[:,2])), color = 'r', label = 'mu-')
        plt.plot(Edep_tau[:,1]*scale_to_kev, ((Edep_tau[:,2]) - np.min(Edep_tau[:,2]))/(np.max(Edep_tau[:,2]) - np.min(Edep_tau[:,2])), color = 'g', label = 'tau-')
        
        plt.legend()
        plt.title('Si')
        plt.xlabel('Energy loss (KeV)')
        plt.ylabel('Energy loss distribution (arb. units)')
        plt.show()

Plots.comparing_meroli_experiment_meroli_simulation()
Plots.comparing_meroli_experiment_g4simulation()
Plots.comparing_meroli_simulation_g4simulation()
Plots.comparing_g4_simulation_materials()
Plots.comparing_g4_simulation_thicknesses()
Plots.comparing_g4_simulation_particles()