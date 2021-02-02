
#ifndef YOURACTIONINITIALIZATION_HH
#define YOURACTIONINITIALIZATION_HH

#include "G4VUserActionInitialization.hh"


// forward declarations
class YourDetectorConstruction;


class YourActionInitialization : public G4VUserActionInitialization {

  // Method declaration:
  public:
    
    // CTR & DTR (you will need to talk to your detector to find out the GUN pos.)
    YourActionInitialization(YourDetectorConstruction* det);
    virtual ~YourActionInitialization(); 

    // (Pure) Virtual method to be implemented by the user to instantiate 
    // User Action class objects
    virtual void Build() const;

    // Virtual method to be implemented by the user to instantiate User RunAction
    // class object to be used by G4MTRunManager. THIS METHOD IS NOT INVOKED IN
    // THE SEQUENTIAL MODE! The user should not use this method to instantiate
    // user action classes rather than user RunAction.
    virtual void BuildForMaster() const;


  // Data member declarations:
  private:

  	YourDetectorConstruction* fYourDetector;
};

#endif