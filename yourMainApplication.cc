// En este modulo se implementa el main que va llamando al resto de
// modulos

#include <iostream>
#include "G4Types.hh"
#include "globals.hh"

#include "G4RunManager.hh"
#include "G4PhysListFactory.hh"

#include "YourDetectorConstruction.hh"
#include "YourPrimaryGeneratorAction.hh"
#include "YourActionInitialization.hh"

#include "G4UImanager.hh"
#include "G4UIExecutive.hh"

#include "G4VisManager.hh"
#include "G4VisExecutive.hh"

int main(int argc, char** argv) {
  
  // Defining UI: 
  G4UIExecutive* ui=0;
  if (argc ==1 ){
    ui = new G4UIExecutive(argc,argv, "qt");
  }

  // Creating the RunManager object 
  G4RunManager* runManager = new G4RunManager();
 
  // Creating an object from YourDetectorConstruction
  YourDetectorConstruction* detector = new YourDetectorConstruction();
  runManager->SetUserInitialization( detector );
   
  // Creating an Physics List
  G4PhysListFactory physListFactory;
  const G4String plName = "FTFP_BERT";
  G4VModularPhysicsList* pl = physListFactory.GetReferencePhysList( plName );
  runManager->SetUserInitialization( pl ); 
  
  // Initializing the detector:
  runManager->SetUserInitialization ( new YourActionInitialization( detector ) );
  
  // initialization of the run
  //  runManager->Initialize();  (comment if you use the UI manager)
 
  // add verbosity
  //  G4EventManager::GetEventManager()->GetTrackingManager()->SetVerboseLevel(1);
  //  G4UImanager* UI = G4UImanager::GetUIpointer();
  //  UI->ApplyCommand("/control/execute g4macro.mac");

  // Visualization
  G4VisManager* visManager = new G4VisExecutive();
  visManager->Initialize();

  // Batch-mode: 
  G4UImanager* UImanager = G4UImanager::GetUIpointer();
  if (!ui) {
    G4String cmd = "/control/execute ";
    G4String scmd = argv[1];
    UImanager->ApplyCommand(cmd + scmd);
  } else {
    ui->SessionStart();
    delete ui;
  }
 
  delete runManager; 
   
  return 0;
}
