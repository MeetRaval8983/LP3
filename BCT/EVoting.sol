// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// Educational e-voting demo for Sepolia testnet only.
contract EVoting {
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    Candidate[] private candidates;
    mapping(address => bool) public hasVoted;
    address public immutable owner;
    bool public votingOpen = true;

    event VoteCast(address indexed voter, uint256 indexed candidateId);

    constructor(string[] memory candidateNames) {
        require(candidateNames.length >= 2, "Add at least two candidates");
        owner = msg.sender;
        for (uint256 i = 0; i < candidateNames.length; i++) {
            candidates.push(Candidate(i + 1, candidateNames[i], 0));
        }
    }

    function vote(uint256 candidateId) external {
        require(votingOpen, "Voting is closed");
        require(!hasVoted[msg.sender], "You have already voted");
        require(candidateId > 0 && candidateId <= candidates.length, "Invalid candidate ID");
        hasVoted[msg.sender] = true;
        candidates[candidateId - 1].voteCount += 1;
        emit VoteCast(msg.sender, candidateId);
    }

    function getCandidate(uint256 candidateId)
        external view returns (uint256 id, string memory name, uint256 voteCount)
    {
        require(candidateId > 0 && candidateId <= candidates.length, "Invalid candidate ID");
        Candidate storage c = candidates[candidateId - 1];
        return (c.id, c.name, c.voteCount);
    }

    function getCandidateCount() external view returns (uint256) {
        return candidates.length;
    }

    function closeVoting() external {
        require(msg.sender == owner, "Only owner");
        votingOpen = false;
    }
}
