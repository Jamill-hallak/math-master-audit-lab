
<p align="center">
  <img src="./images/math-master.png" width="400" alt="math-master" />
</p>

# 🧠 Math Masters Audit Lab

This repository is a professional showcase of formal verification, low-level math, and test-driven development, combining Solidity, Certora, Halmos, and fuzz testing.

> ⚙️ **Inspired by**:  
> [Solmate](https://github.com/transmissions11/solmate), [Solady](https://github.com/Vectorized/solady), [obront.eth](https://twitter.com/zachobront), and built with insights from Cyfrin's [Updraft FV course](https://updraft.cyfrin.io/).  
>  
> 👥 Special thanks to [karma](https://twitter.com/0xkarmacoma) for guidance on Certora-based formal verification.

---

## 📌 About

This lab dissects gas-efficient math operations and verifies correctness through formal specs, unit tests, and edge case exploration.

We evaluate critical functions such as:

- `mathMasterTopHalf(x)`
- `sqrt(x)`

and verify their equivalence against trusted references (e.g., Solmate).

---

## 🚀 Getting Started

### Requirements

- [Git](https://git-scm.com/)
- [Foundry](https://getfoundry.sh/)
- [Python 3](https://www.python.org/) & [pipx](https://github.com/pypa/pipx)
- [Certora CLI](https://docs.certora.com/en/latest/docs/user-guide/getting-started/install.html)
- [Halmos](https://github.com/a16z/halmos)

```bash
git --version        # git version x.x.x
forge --version      # forge 0.2.0 or newer
certoraRun --version # certora-cli 6.x.x
halmos --version     # halmos 0.1.x
```

---

## ⚡ Quickstart

```bash
git clone https://github.com/Jamill-hallak/math-master-audit-lab
cd math-master-audit-lab
make
```

---

## 🧪 Usage

### Run Tests

```bash
forge test
```

### View Coverage

```bash
forge coverage
forge coverage --report debug
```

---

## 🔍 Formal Verification (FV)

### Certora

- `Sqrt.spec` verifies edge cases for square root logic
- `mulWadUp.spec` checks safe multiplication with WAD precision
- All configs are under `/certora`

### Halmos

Halmos is used to verify math correctness with `assertEq` in simulated environments.

---

## 🧩 Audit Scope

```txt
Contract: MathMasters.sol
Main Logic: sqrt, mathMasterTopHalf
```

- ✅ Commit: `c7643faa1a188a51b2167b68250816f90a9668c6`
- ✅ Compatible with: Ethereum Mainnet, Solc 0.8.x

---

## 📚 Project Layout

```
certora/
├── mulWadUp.conf / .spec
├── Sqrt.conf / .spec

src/
└── MathMasters.sol

test/
├── Base_Test.t.sol
├── harness.sol
└── MathMasters.t.sol
```

---

## 🧠 Author

Made with ❤️ by [Jamil Hallack](https://github.com/Jamill-hallak), Security Researcher & Formal Verification Specialist.

---

> ⭐ Star this repo if you're passionate about secure and optimized smart contracts!
