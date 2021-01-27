#include "globals.hh"
#include "YourPrimaryGeneratorAction.hh"
#include "YourDetectorConstruction.hh"
#include "G4Material.hh"


YourPrimaryGeneratorAction:YourPrimaryGeneratorAction(YourDetectorConstruction* det):
  G4UserPrimaryGeneratorAction() {
  fYourDetector = det;
  G4cout<< det->GetTargetMaterial() << G4endl;
}

YourPrimaryGeneratorAction::~YourPrimaryGeneratorAction(){}

void YourPrimaryGeneratorAction::GeneratePrimaries(G4Event* anEvent) {}
