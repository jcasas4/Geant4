
#ifndef YOUREVENTACTION_HH
#define YOUREVENTACTION_HH

#include "G4UserEventAction.hh"

#include "globals.hh"

class YourEventAction : public G4UserEventAction {

  // Method declaration:
  public:
    
    // CTR: 
    YourEventAction();
    virtual ~YourEventAction();

    // Two virtual method called at the beginning and at the end of each event 
    virtual void BeginOfEventAction(const G4Event* anEvent);
    virtual void EndOfEventAction(const G4Event* anEvent);

    // Public method (used by the SteppingAction) to add energy deposit and 
    // charged particle track length information to this object after each step.
    void AddEnergyDepositPerStep(const G4double edepAlongTheStep) { 
        fEdepPerEvt += edepAlongTheStep;
    }
    void AddChargedTrackLengthPerStep(const G4double trackLAlongTheStep) { 
    	fChTrackLengthPerEvt += trackLAlongTheStep;
    }

  // Data member declarations:
  private:
    
    G4double   fEdepPerEvt;
    G4double   fChTrackLengthPerEvt;

};

#endif