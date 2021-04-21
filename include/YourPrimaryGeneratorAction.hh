// En este modulo se definen las clases y metodos necesarios para 
// implementar la accion en el detector en YourPrimaryGeneratorAction.cc

#ifndef YOURPRIMARYGENERATORACTION_HH
#define YOURPRIMARYGENERATORACTION_HH

#include "G4VUserPrimaryGeneratorAction.hh"

#include "globals.hh"

// forward declaration
class YourDetectorConstruction;
class G4ParticleGun;
class G4Event;
class G4String;


class YourPrimaryGeneratorAction : public G4VUserPrimaryGeneratorAction {

  // Method declaration:
  public:
    
    // CTR & DTR
    YourPrimaryGeneratorAction(YourDetectorConstruction* det);
    virtual ~YourPrimaryGeneratorAction();

    // (Pure) virtual method to generata primary events
    virtual void   GeneratePrimaries(G4Event*);

    //
    // Additional custom methods: 

    // Public method to obtain the G4ParticleGun object pointer and some other 
    // primary particle realted values
    G4ParticleGun*  GetParticleGun() { return fParticleGun; }

    // Public method to get the primary particle name.
    const G4String& GetParticleName() const;

    // Public method to get the primary particle kinetic energy.
    G4double        GetParticleEnergy() const;

    // Public method to set the default primary particle kinematics
    void            SetDefaultKinematic();

    // Public method to set the position of the particle gun: will be taken for
    // the actual detector construction
    void            UpdatePosition();


  // Data member declarations:
  private:

  	YourDetectorConstruction* fYourDetector;

  	G4ParticleGun*            fParticleGun; 

};

#endif
