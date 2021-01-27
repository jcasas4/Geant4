#ifndef YOURPRIMARYGENERATORACTION_HH
#define YOURPRIMARYGENERATORACTION_HH

#include "G4VUserPrimaryGeneratorAction.hh"

class YourPrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction {
public: 
  
  YourPrimaryGeneratorAction(YourDetectorConstruction *det); 
  ~YourPrimaryGeneratorAction();
  
  virtual void GeneratePrimaries(G4Event* anEvent);

private: 
  YourDetectorConstruction* fYourDetector;
}
#endif
