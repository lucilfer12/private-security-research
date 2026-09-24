# Threat Modeling

For every case define:

### Assets
What can be forged, stolen, frozen, corrupted, or made unavailable?

### Actors
Untrusted user, authenticated user, relayer, operator, governance, emergency administrator.

### Trust boundaries
Mark transitions between accounts, services, chains, cryptographic domains, and privileged components.

### Attacker capabilities
State exactly what the attacker controls and cannot control.

### Failure modes
Cryptographic key collision, authorization failure, replay, stale state, arithmetic error, inconsistent cross-domain state, or unsafe configuration.

### Recovery
Can the system rotate credentials, revoke access, pause operations, or repair affected state?
