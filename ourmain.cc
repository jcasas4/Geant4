#include <iostream>
#include "G4Types.hh"
#include "globals.hh"

// HERE 
#include "G4NistManager.hh"
#include "G4RunManager.hh"

#include "G4PhysListFactory.hh"

#include "YourDetectorConstruction.hh"
#include "YourPrimaryGeneratorAction.hh"


int main() {
  
  //1. create the RunManager object 
  G4RunManager* runManager = new G4RunManager();
 
  //2. Create an object from YourDetectorConstruction and register in the Run-Manager
  YourDetectorConstruction* detector = new YourDetectorConstruction();
  runManager->SetUserInitialization( detector );
   
  //3. Create/obtain an Physics List and register it in the Run-Manager 
  G4PhysListFactory physListFactory;
  const G4String plName = "FTFP_BERT";
  G4VModularPhysicsList* pl = physListFactory.GetReferencePhysList( plName );
  runManager->SetUserInitialization( pl ); 
  
  //4. Create your action initizalizatio and register in the Run Manager:
  runManager->SetUserInitialization ( new YourPrimaryGeneratorAction( detector ) );
  
  // initialization of the run
  runManager->Initialize();

  // add verbosity
  G4EventManager::GetEventManager()->GetTrackingManager()->SetVerboseLevel(1);
  
  // simulate 10 events
  runManager->BeamOn(10); 
   
  // delete the Run-manager
  delete runManager; 
   
  return 0;
}
