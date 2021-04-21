// En este modulo se definen las clases y metodos necesarios para 
// implementar la accion en el detector en YourRunAction.cc

#ifndef YOURRUNACTION_HH
#define YOURRUNACTION_HH

#include "G4UserRunAction.hh"

#include "G4String.hh"

// forward declarations
class YourPrimaryGeneratorAction;
class G4Run;


class YourRunAction : public G4UserRunAction {

  // Method declaration:
  public:
    
    // CTR: 
    //  - detector construction object is used in the stepping action to check target
    //  - primary generator is used to re-set position for workers and to get E0 (set only for workers)
    YourRunAction(YourPrimaryGeneratorAction* prim = nullptr);
    virtual ~YourRunAction();

    // Virtial method that is called by the RunManager before the first event starts
    virtual void   BeginOfRunAction(const G4Run*);

    // Virtual method that is called by the RunManager after the last event finished
    virtual void   EndOfRunAction(const G4Run*);

  // Data member declarations:
  private:

  	YourPrimaryGeneratorAction*  fYourPrimary;     
};

#endif
